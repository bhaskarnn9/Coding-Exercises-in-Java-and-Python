import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class LC88 {
    public static void main(String[] args) {
        List<Integer> nums1 = new ArrayList<>(Arrays.asList(1, 2, 4, 7, 8, 9));
        List<Integer> nums2 = Arrays.asList(0, 3, 3, 5, 8);

        int m = nums1.size(); // get the length before modifying
        int n = nums2.size();
        for (int i = 0; i < n; i++) {
            nums1.add(0);
        }
        System.out.println("Before merging, nums1: " + nums1);
        mergeSortedArrays(nums1, nums2, m, n);
        System.out.println("After merging, nums1: " + nums1);

    }

    public static void mergeSortedArrays(List<Integer> nums1, List<Integer> nums2, int m, int n) {

        int i = m - 1; // 5
        int j = n - 1; // 4
        int k = m + n - 1; // 10

        while (j >= 0) {
            if (i >=0 && nums1.get(i) > nums2.get(j)) {
                nums1.set(k, nums1.get(i));
                i--;
            } else {
                nums1.set(k, nums2.get(j));
                j--;
            }
            k--;
        }
    }
}