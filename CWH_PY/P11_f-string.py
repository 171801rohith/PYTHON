# String Formatting in Python

# Before
letter = "Hey I'm {1} and I'm from {0}"
country = "India"
name = "Rohith"
print(letter.format(country, name))
letter = "Hey I'm {} and I'm from {}"
print(letter.format(name, country))

# Now
country1 = "India"
name1 = "Rohith"
country2 = "USA"
name2 = "Rohh"
print(f"I'm {name} and I'm from {country}")

price = 49.898980
print(
    f"The price is {price:.2f}"
)  # here '.nf' helps to round-off num to n decimal place
print(f"{2 * 6}")

country1 = "India"
name1 = "Rohith"
country2 = "USA"
name2 = "Rohh"
print(f"{country1} : {name1}")
print(f"{country2} : {name2}")
print(f"{{country2}} : {{name2}}")

# public class noth {
#     public static void main(String[] args) {
#         String[] strs = { "aadithya", "rohith", "yash", "ramakrishna" };
#         int[] marks = { 20, 30, 40, 29 };
#         for (int i = 0; i < strs.length; i++) {
#             System.out.format("%-15s:%4d\n", strs[i], marks[i]);
#         }
#     }
# }

strs = ["aadithya", "rohith", "yash", "ramakrishna"]
marks = [20, 30, 40, 29]

for i in range(len(strs)):
    print(f"{strs[i]:<15}:{marks[i]:>4}")
   
    # System.out.format("%-15s:%4d\n", strs[i], marks[i]);
    
for i in range(len(strs)):
    print(f"{strs[i]:>15}:{marks[i]:>4}")
    # System.out.format("%15s:%4d\n", strs[i], marks[i]);