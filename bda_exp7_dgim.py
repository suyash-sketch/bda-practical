class DGIM:
    def __init__(self):
        self.timestamp = 0
        # duckets are stored newest to oldest
        self.buckets = []

    def add(self, bit):
        self.timestamp +=1

        if bit == 1:
            self.buckets.insert(0, (1, self.timestamp))
            self.merge_buckets()


    def merge_buckets(self):

        while True:
            size_indices = {}

            for index, (size, _) in enumerate(self.buckets):
                size_indices.setdefault(size, []).append(index)

            size_to_merge = None

            for size, indices in size_indices.items():
                if len(indices) > 2:
                    size_to_merge = size
                    break

            if size_to_merge is None:
                break

            # merge the two oldest buckets of this size
            indices = size_indices[size_to_merge]
            second_oldest = indices[-2]
            oldest = indices[-1]

            timestamp = self.buckets[second_oldest][1]
            self.buckets[second_oldest] = ( size_to_merge * 2, timestamp)
            self.buckets.pop(oldest)


    def count_last(self, n):
        if n <= 0:
            return 0

        window_start = max(1, self.timestamp - n + 1)

        # select buckets whose newest bit lies in the window
        relevant_buckets = [
            bucket for bucket in self.buckets if bucket[1] >= window_start
        ]

        if not relevant_buckets:
            return 0

         # count all buckets,
         # then subtract half of the oldest relevant bucket to estimate its overlap
        count = sum( size for size, _ in relevant_buckets)
        count -= relevant_buckets[-1][0] / 2

        return round(count)

stream = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

dgim = DGIM()

for bit in stream:
    dgim.add(bit)

print("Stream:", stream)
print("Estimated 1s in last 5 bits:", dgim.count_last(5))
print("Estimated 1s in last 10 bits:", dgim.count_last(10))
print("Buckets:", dgim.buckets)
