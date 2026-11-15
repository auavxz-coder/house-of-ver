-- HOUSE OF VÈR gift options: run once in Supabase SQL Editor
-- These columns are optional; existing orders remain unchanged.
alter table public.orders
  add column if not exists is_gift boolean not null default false;
alter table public.orders
  add column if not exists gift_message text;
alter table public.orders
  add constraint gift_message_length check (char_length(gift_message) <= 300);
