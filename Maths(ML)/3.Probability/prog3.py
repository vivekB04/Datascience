#conditional Probability and Bayes theroem

p_spam =0.1
p_offer_given_spam=0.8
p_offer_given_safe=0.05
p_safe=0.9

p_offer = (p_offer_given_spam * p_spam) + (p_offer_given_safe * p_safe)

p_spam_given_offer= (p_offer_given_spam *p_spam)/ p_offer

print(f"Probability Its spam given the word 'Offer' : {p_spam_given_offer:.2%}")