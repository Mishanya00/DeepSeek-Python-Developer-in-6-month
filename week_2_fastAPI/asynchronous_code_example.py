import asyncio
from random import randint

async def make_burger(order_id: int):
    """Emulate a time-consuming task"""
    cook_time = randint(1, 5)
    print(f"🍔 [Order {order_id}] Started cooking (will take {cook_time}s)...")
    await asyncio.sleep(cook_time)  # Non-blocking wait
    print(f"✅ [Order {order_id}] Burger ready!")

async def take_orders(count: int):
    """Async cashier that handles multiple orders without freezing."""
    tasks = []
    for order_id in range(1, count+1):
        print(f"📝 [Order {order_id}] Taken by cashier.")
        task = asyncio.create_task(make_burger(order_id))  # Start kitchen work
        tasks.append(task)
    
    await asyncio.gather(*tasks)  # Wait for all burgers to finish


orders_count = int(input("Number of orders: "))

print("🏁 START: Cashier starts taking orders.")
asyncio.run(take_orders(orders_count)) # Run the async workflow
print("🛑 END: All orders completed.")