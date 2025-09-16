# Cofi Code Challenge

Besides our SaaS, Cofi also wants to run a physical store which sells 3 products (by now):

```
Code         | Name              |  Price
-------------------------------------------------
VOUCHER      | Cofi Voucher      |   5.00€
TSHIRT       | Cofi T-Shirt      |  20.00€
MUG          | Cofi Coffee Mug   |   7.50€
```

Various departments have insisted on the following discounts:

- The marketing department believes in 2-for-1 promotions (buy two of the same product, the second one is free), and would like for there to be a 2-for-1 special on `VOUCHER` items.
- The CFO insists that the best way to increase sales is with discounts on bulk purchases (buying x or more of a product, the price of that product is reduced), and demands that if you buy 3 or more `TSHIRT` items, the price per unit should be 19.00€.
- John from accounting wants to include a SWAG discount, that is: a SWAG is a pack which consists in a TSHIRT + VOUCHER + MUG and has a fixed price of 25€.

Cofi's checkout process allows for items to be scanned in any order, and should return the total amount to be paid. The interface for the checkout can look like this (Typescript):

```tsx
// We only need two public methods: scan and total
interface Checkout {
  scan: (sku: string) => void;
  total: () => number;
}

// Usage
const { scan, total } = useCheckout();
scan("VOUCHER");
scan("VOUCHER");
scan("VOUCHER");
scan("TSHIRT");
scan("MUG");
const totalAmount = total();
console.log(totalAmount); // 30.00
```

Our sales team is constantly adding, removing, and repricing products, so they should be configurable with a json file.

**Notes about the solution**

You can use any programming language and style you want, we recommend you to use the one you feel more comfortable with. Make sure to include instructions of how to run it and clarify any part of the solution you consider is not obvious.

As long as the functionality is preserved you can modify the suggested interface to suit your design/style/programming language of choice.

The code should be written as if it would be part of a bigger piece of code which is already running in production - i.e. we don't need it to be a full fledge standalone service - but it should pass a code review.

In our code reviews there are 3 things we check first:

- Does it work according to the specs?
- Is it properly tested?
- Is the solution self-describing/easy to understand/well documented?

Asking questions to understand the problem is always better than implementing the right solution for the wrong problem.
