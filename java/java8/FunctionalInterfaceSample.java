package java8;

@FunctionalInterface
interface StringModifier {
    String modify(String str);
}
class FunctionalInterfaceSample {

    public static void main(String[] args) {
        // Define lambda expression for uppercase conversion
        StringModifier toUpper = str -> str.toUpperCase();

        // Use the lambda expression with the interface method
        String modifiedString = toUpper.modify("Hello World!");
        System.out.println(modifiedString); // Output: HELLO WORLD!

        // Define another lambda expression for removing vowels
        StringModifier removeVowels = str -> str.replaceAll("[aeiou]", "");

        // Use the second lambda expression
        String withoutVowels = removeVowels.modify("This is a string");
        System.out.println(withoutVowels); // Output: Ths s  strng
    }
}
