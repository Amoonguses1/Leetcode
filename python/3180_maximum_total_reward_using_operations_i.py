# Time: O(MN)
# Space: O(MN)
# M is the maximum value among rewardValues
# N = len(rewardValues)
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewards = sorted(list(set(rewardValues)))
        ans = {0}
        for reward in rewards:
            new_rewards = set()
            for val in ans:
                if val < reward:
                    new_rewards.add(val+reward)
            ans.update(new_rewards)
        return max(ans)
