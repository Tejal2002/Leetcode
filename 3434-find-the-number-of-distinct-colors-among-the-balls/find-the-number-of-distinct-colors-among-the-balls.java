class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        int n = queries.length;
        int[] result = new int[n];

        Map<Integer, Integer> ballColors = new HashMap<>(); // Maps ball -> color
        Map<Integer, Integer> colorCount = new HashMap<>(); // Tracks frequency of each color

        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int newColor = queries[i][1];

            // If ball already has a color, update color count
            if (ballColors.containsKey(ball)) {
                int oldColor = ballColors.get(ball);
                colorCount.put(oldColor, colorCount.get(oldColor) - 1);

                // If the old color is no longer present, remove it from the map
                if (colorCount.get(oldColor) == 0) {
                    colorCount.remove(oldColor);
                }
            }

            // Assign the new color to the ball
            ballColors.put(ball, newColor);

            // Update color count for newColor
            colorCount.put(newColor, colorCount.getOrDefault(newColor, 0) + 1);

            // Store the number of distinct colors
            result[i] = colorCount.size();
        }

        return result;
  
    }
}