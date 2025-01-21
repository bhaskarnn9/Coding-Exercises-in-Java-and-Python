import java.util.Arrays;

class LC27 {
    // Helper method to handle the removal logic
    private int helper(int[] nums, int val, int pointer) {
        boolean flag = false;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val) {
                flag = true;
                int temp = nums[pointer];
                nums[i] = temp;
                nums[pointer] = -1; // Use -1 to represent the removed element (similar to '_')
                pointer--;
                break;
            }
        }

        if (flag) {
            return helper(nums, val, pointer); // Recursive call
        }

        return pointer;
    }

    // Main function to remove the element and return the updated length
    public int removeElement(int[] nums, int val) {
        int pointer = nums.length - 1;
        pointer = helper(nums, val, pointer); // Call the helper function
        return pointer + 1; // Return the new length of the array
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums = {3, 2, 2, 3};
        int val = 3;

        System.out.println("Before removal: " + Arrays.toString(nums));
        int newLength = solution.removeElement(nums, val);
        System.out.println("After removal: " + Arrays.toString(nums));
        System.out.println("New length: " + newLength);
    }
}