# crowdfunding-api
This is a web api for crowdfunding workflows. (Based of Stripe)

#Notes
We use Stripe as our payment system. We don't store any financial information, only the Stripe's keys.

The main concepts here are:
Account: Where all the payments are going to be received. We use managed accounts from Stripe.
Payment: The credit card payment


For now we only support 1 workflow:
 - We collect payments (Fixed payments).
 - If the goal is reached we processed all payments and transfer the money to the account.
