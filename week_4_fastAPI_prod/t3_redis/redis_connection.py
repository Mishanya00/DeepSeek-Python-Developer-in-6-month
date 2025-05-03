import redis

# You should launch redis on localhost:6379 beforehand!
# In case of Windows OS you should create Docker Redis container
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(host='localhost', port=6379, decode_responses=False)


print('First addition:', r.set('foo', 'bar'))
print('Second addition:', r.set('foo', 'bar'))

print(r.get('foo'))

print(r.delete('foo'))
print(r.delete('foo'))

print(r.get('foo'))


r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

print(r.hgetall('user-session:123'))

r.hdel('user-session:123', 'company')

print(r.hgetall('user-session:123'))

r.delete('user-session:123')

print(r.hgetall('user-session:123'))