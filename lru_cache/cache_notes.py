# NOTES

'''
What are caches?
    - Bits of storage that are fast to access that keep small amounts of frequently used data in them
    - Primary storge (slow, hard drive) --> Cache (fast, frequently used file stored) --> User
    
    DEF's:

        Cache Hit: when the data you want is in the cache
        Cache Miss: When you have to go to primary storage to get the data


What are LRU caches, and how are they built?
    (Least Recently Used)
    - Caches are limited in size compared to primary storage
        - Need some strategy to remove items from the cache because we have a smaller limited space vs primary storage -- hopefully ones that we dont need in the future very often
    - LRU caches discard the Least-Recently-Used item in the cache when it is full (since it's the lrc, its probably one of the least important things...)

Building
Put, get, and delete
    - You want to be able to look something up by a 'key' (ie a string)
    - Then you will want to look in the cache and see if the data corresponding to that key exists -- similar to a has table

    - Need a hash table to quickly look up cache entries by key
        - take a key and pass it into the hash table, then the hash table will quickly return a result for that key
        - They do this in O(1) time complexity

    - Need the cache entries in a doubly-linked-list
        - we will have our cache entries stored in memory and they will all be conected by a DLL along with our hash table that points to every element in the DLL
        - O(1) with moving items around in it (ie to the head) and removing (ie from the tail)

PUT:
    - Move the head of the list
    - Add hash table entry (MRU)
    - If over-full:
        - simply delete the tail entry from the DLL and the hash table

GET:
    - Move the accessed element to the head of the list (MRU)
    - Then return a pointer to that entry
    - If over-full:
        - simply delete the tail entry from the DLL and the hash table





CHALLENEGE QUESTIONS:

What are some applications of LRU caches?

    - example from interview cake:
        - managing a cooking site with a lot of cake recipes and you want to serve up pages AFAP

How would you add functionality to the cache? (in psuedocode) to remove entries that are older that a cutoff age from the cache? O(n) time is OK
    - 

How would you remove entries as above O(1) time? 

    - look up the item in hash map
    - if the item is in the hash table, then it's already in our cache -- CACHE HIT
        - use hash to find corresponding linked list node
        - move the items LL node to the head since is MRU now
    - if the items is NOT in hash table -- CACHE MISS -- we need to load the item into the cach
        - is the cache full? 
            - then evict the LRU (tail) by removing it from the LL and the hash map
    - Create new LL node for the item and insert it at the head of LL
    - Add the item to the hash map, storing the newly-created LL node as the value


'''