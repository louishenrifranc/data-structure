class HashMap:
    INITIAL_NUM_BUCKET = 3
    RATIO_OCCUPANCY_FOR_EXPANSION = 0.8

    def __init__(self, num_buckets=None):
        self._num_buckets = num_buckets or HashMap.INITIAL_NUM_BUCKET
        self.occupied_buckets = 0

        self.buckets = [None] * self._num_buckets

    def _should_expand(self):
        return self.occupied_buckets / self._num_buckets > HashMap.RATIO_OCCUPANCY_FOR_EXPANSION

    def hash(self, value):
        return int(hash(value)) % (self._num_buckets - 1)

    def expand(self):
        if not self._should_expand():
            return
        keys, values = self._dump_pairs()

        self._num_buckets *= 2
        self.buckets = [None] * self._num_buckets
        self.occupied_buckets = 0

        self.setitems(keys, values)

    def _dump_pairs(self):
        keys, values = list(), list()
        for bucket in self.buckets:
            if bucket is not None:
                for bucket_entry in bucket:
                    keys.append(bucket_entry[0])
                    values.append(bucket_entry[1])
        return keys, values

    def setitems(self, keys, values):
        for key, value in zip(keys, values):
            self[key] = value

    def __setitem__(self, new_key, new_value):
        bucket_id = self.hash(new_key)
        new_entry = [new_key, new_value]

        if self.buckets[bucket_id] is None:
            self.buckets[bucket_id] = list([new_entry])
        else:
            for bucket_entry in self.buckets[bucket_id]:
                if bucket_entry[0] == new_entry[0]:
                    bucket_entry[1] = new_entry[1]
            self.buckets[bucket_id].append(new_entry)
        self.occupied_buckets += 1

        self.expand()

    def __getitem__(self, key):
        hash_key = self.hash(key)
        if self.buckets[hash_key] is not None:
            for bucket_entry in self.buckets[hash_key]:
                if bucket_entry[0] == key:
                    return bucket_entry[1]
        raise KeyError("{} is not in dict".format(key))
