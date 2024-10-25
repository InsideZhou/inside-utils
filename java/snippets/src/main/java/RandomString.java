import java.util.Random;
import java.util.stream.IntStream;

public class RandomString {
    public static final String CHAR_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    public static String generate() {
        return generate(16);
    }

    public static String generate(int length) {
        var sb = new StringBuilder(length);
        var random = new Random();

        IntStream.range(0, length).forEach(i ->
            sb.append(CHAR_POOL.charAt(random.nextInt(CHAR_POOL.length())))
        );

        return sb.toString();
    }

    public static void main(String[] args) {
        try {
            System.out.println(generate(Integer.parseInt(args[0])));
        }
        catch (Exception e) {
            System.out.println(generate());
        }

    }
}
