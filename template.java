import java.io.*;
import java.util.*;

public class template {
    private void solve() throws NumberFormatException, IOException {
        // TODO: write solution
    }
    
    // template below this point
    
    private static final String taskname = template.class.getSimpleName();

    private StringTokenizer strtok;
    private BufferedReader inr;
    private PrintWriter out;

    public static void main(String[] args) {
        (new template()).run();
    }

    private void run() {
        Locale.setDefault(Locale.US);
        boolean oj = System.getProperty("ONLINE_JUDGE") != null;
        try {
            inr = new BufferedReader(oj ? new InputStreamReader(System.in, "ISO-8859-1") : new FileReader(taskname + ".in"));
            out = new PrintWriter(oj ? new OutputStreamWriter(System.out, "ISO-8859-1") : new FileWriter(taskname + ".out"));
            solve();
        } catch (Exception e) {
            if (!oj)
                e.printStackTrace();
            System.exit(9000);
        } finally {
            out.flush();
            out.close();
        }
    }

    private String nextToken() throws IOException {
        while (strtok == null || !strtok.hasMoreTokens()) {
            strtok = new StringTokenizer(inr.readLine());
        }
        return strtok.nextToken();
    }

    private int nextInt() throws NumberFormatException, IOException {
        return Integer.parseInt(nextToken());
    }

    private long nextLong() throws NumberFormatException, IOException {
        return Long.parseLong(nextToken());
    }

    private double nextDouble() throws NumberFormatException, IOException {
        return Double.parseDouble(nextToken());
    }
}
