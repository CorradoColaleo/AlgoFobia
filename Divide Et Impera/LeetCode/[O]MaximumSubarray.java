package LeetCode;

class Solution {

    public static int maxSubArrayDivideEtImpera(int[] nums) {

        return maxSum(nums, 0, nums.length-1);

    }

    public static int maxSum(int [] nums, int l, int r) {

        if (l<r) {

            int q = (l+r)/2;

            int maxLeftSum = maxSum(nums, l, q);

            int maxRightSum = maxSum(nums, q+1, r);

            int maxMerge = maxSumMerge(nums, l, q, r);

            return Math.max(Math.max(maxLeftSum, maxRightSum), maxMerge);

        }
        else {

            return nums[l];
        }

    }

    public static int maxSumMerge(int [] nums, int l, int q, int r) {

        int leftMax = nums[q];

        int leftSum = nums[q];

        int rightMax = nums[q+1];

        int rightSum = nums[q+1];

        int i;

        for (i=q+2;i<=r;i++) {

            rightSum += nums[i];

            if (rightMax<rightSum) {

                rightMax = rightSum;
            }

        }

        for (i=q-1;i>=l;i--) {

            leftSum += nums[i];

            if (leftMax<leftSum) {

                leftMax = leftSum;
            }

        }

        return leftMax + rightMax;

    }

    public static void main(String[] args) {

        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};

        int result = maxSubArrayDivideEtImpera(nums);

        System.out.println("Result: " + result);
        
    }
}