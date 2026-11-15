-- HOUSE OF VÈR: safe account-owned order detail retrieval
-- Run once in Supabase SQL Editor.
create or replace function public.my_order_details(requested_order_id text)
returns jsonb
language sql
security definer
set search_path = ''
stable
as $$
  select jsonb_build_object(
    'order_id', o.order_id,
    'created_at', o.created_at,
    'quantity', o.quantity,
    'subtotal', o.subtotal,
    'delivery_fee', o.delivery_fee,
    'total', o.total,
    'emirate', o.emirate,
    'area', o.area,
    'payment_status', o.payment_status,
    'fulfillment_status', o.fulfillment_status
  )
  from public.orders o
  where o.order_id = requested_order_id
    and o.user_id = (select auth.uid())
  limit 1;
$$;
revoke all on function public.my_order_details(text) from public, anon;
grant execute on function public.my_order_details(text) to authenticated;
