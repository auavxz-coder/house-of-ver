-- Run in Supabase SQL Editor before enabling customer accounts.
create table if not exists public.customer_profiles (
 user_id uuid primary key references auth.users(id) on delete cascade,
 cart_qty integer not null default 0 check(cart_qty between 0 and 20),
 full_name text, phone text, instagram text, address text, emirate text, area text,
 updated_at timestamptz not null default now()
);
alter table public.customer_profiles enable row level security;
revoke all on public.customer_profiles from anon;
grant select, insert, update on public.customer_profiles to authenticated;
drop policy if exists "Customers read own profile" on public.customer_profiles;
create policy "Customers read own profile" on public.customer_profiles for select to authenticated using (auth.uid()=user_id);
drop policy if exists "Customers insert own profile" on public.customer_profiles;
create policy "Customers insert own profile" on public.customer_profiles for insert to authenticated with check (auth.uid()=user_id);
drop policy if exists "Customers update own profile" on public.customer_profiles;
create policy "Customers update own profile" on public.customer_profiles for update to authenticated using (auth.uid()=user_id) with check (auth.uid()=user_id);

alter table public.orders add column if not exists user_id uuid references auth.users(id) on delete set null;
create index if not exists idx_orders_user_id on public.orders(user_id);
-- Never grant direct read of orders to customers.
revoke all on public.orders from anon, authenticated;

create or replace function public.my_order_summaries()
returns table(order_id text, created_at timestamptz, total numeric, payment_status text, fulfillment_status text)
language sql security definer set search_path = ''
as $$
 select o.order_id,o.created_at,o.total,o.payment_status,o.fulfillment_status
 from public.orders o where o.user_id = (select auth.uid())
 order by o.created_at desc limit 50;
$$;
revoke all on function public.my_order_summaries() from public, anon;
grant execute on function public.my_order_summaries() to authenticated;
