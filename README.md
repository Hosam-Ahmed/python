# python
Stock Management Program
- I have developed a "Stock Management program" for a computer store that stores and manages products listed for sale. 
- It stores each product with five attributes barcode, category, brand, price, and quantity at hand.
- The program stores two attributes: code and quantity of each product along with other attributes. 
- As code is the unique identifier, the program ensures that each product is stored with a unique code value. 
- The program will only accept the quantity of a new product between 10 and 50 to ensure there are enough quantities available of a product for sale and, they are not overstocked.

Functions:

1: addProduct() 
function addProduct() reads and stores product information into  lists. This 
function  allows a  user  to  add  as  many  products  they  want  to  add  for  sale.
 This function shows an error message if a user wants to add new product with existing 
code value.

2: checkProduct()
checkProduct() checks  if  a product exists or not. It receives an input argument (code) and return Boolean 
(True  or  False)  value.  It returns  true  if  it  finds  an  existing  product  with  the  given 
code otherwise returns false. 
Note: This function checkProduct() is not part of the main menu options but it 
will be used by other functions or the main program every time a check is required on the 
Product ID by taking the Product ID as an input argument from the other functions or the 
main program. 

3: searchProduct()
searchProduct() searchs a product by code.  This function receives an input argument (code) and it 
uses the checkProduct function to ensure the product code exists before displaying 
the details of the product matching the given product code. 
 This function continuously displays an error message if a user tries to search a 
product with wrong code.

4: updateProduct()
updateProduct() updates a product. This function receives an input argument (code) to check if the product code exists before allowing any update. 
As code is read only value, this function does not allow user to update the code value.
Note: This function calls the searchProduct() to search the product code and display its details before asking the user for what to update.

5: buyProduct()
“buyProduct” that will be called when a customer wants to buy a product form the store. This function receives two 
arguments:  code  and  quantity.  The  function validates the  product  code  using checkProduct function and should validate the quantity values before accepting them to 
calculate the total price. 
The total price (quantity * price of the product) will include Goods and Services Tax (GST) amount  as  well  where  the  GST  rate  is  15%  of  the  total  price. business  wants  to increase the sale so an offer following discount on full GST inclusive price:

10% discount When a customer buys between 10 and 20 quantities of a 
products (including the 10 but less than 20).

20% discount When a customer buys between 20 and 30 quantities of a 
products (inclusive).

30% discount When  a  customer  buys  more  than  30  quantities  of  a 
products

After a customer buys a product, its quantity value will be updated to reflect the actual 
number of product quantities available for sale.
