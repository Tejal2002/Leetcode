import java.util.ArrayList;
import java.util.List;

class ProductOfNumbers {
    private List<Integer> prefixProducts;

    public ProductOfNumbers() {
        prefixProducts = new ArrayList<>();
        prefixProducts.add(1); // Initialize with 1 to handle division correctly
    }

    public void add(int num) {
        if (num == 0) {
            // Reset the prefix products list when a zero is encountered
            prefixProducts = new ArrayList<>();
            prefixProducts.add(1);
        } else {
            // Compute prefix product
            int lastProduct = prefixProducts.get(prefixProducts.size() - 1);
            prefixProducts.add(lastProduct * num);
        }
    }

    public int getProduct(int k) {
        int n = prefixProducts.size();
        if (k >= n) {
            return 0; // If k exceeds available numbers (due to zero), return 0
        }
        return prefixProducts.get(n - 1) / prefixProducts.get(n - k - 1);
    }
}

/**
 * Example usage:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int result = obj.getProduct(k);
 */
