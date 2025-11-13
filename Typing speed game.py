import random,time

print("Welcome to the Typing Speed Test!!".center(175,'*'))
l1=['Happiness is not something we can buy or touch.',' it is a feeling that comes from within.',
    'It is the peace of mind we feel when we are content with who we are and what we have.'
    ,' Many people think happiness depends on money, success or luxury, but true happiness comes from simple things like spending time with loved ones, helping others, being grateful and having a positive attitude.',' Happiness grows when we share it because a smile or kind word can make someone’s day brighter and fill our hearts with joy.',' Challenges and failures are a part of life, but staying hopeful through them makes us stronger and happier.',' So, let us choose to be happy every day, appreciate life’s little moments and spread joy wherever we go.',
    'Kindness is one of the most beautiful qualities a person can have.',
    ' It means being gentle, understanding, and caring toward others without expecting anything in return.',
    ' A small act of kindness, like offering help, listening to someone’s problems, or simply smiling, can make a big difference in someone’s day.',
    ' True kindness comes from the heart; it does not depend on wealth, status, or power.',
    ' It is a language that everyone understands, no matter their age, culture, or background.',
    'When we are kind, we create a ripple effect that spreads positivity and inspires others to do the same. ',
    'In today’s fast-paced world, where people are often busy and stressed, kindness reminds us of our shared humanity.',
    'It helps build stronger relationships and brings peace to our minds. Being kind also makes us happier, because helping others gives a deep sense of satisfaction.',
    ' Even a small gesture of kindness can change lives and make the world a better place to live in.',
'Trust is the foundation of every strong relationship, whether it is between friends, family members, or colleagues.',
    ' It means having faith in someone’s honesty, reliability, and intentions.',
    ' When there is trust, people feel safe to share their thoughts and emotions without fear of being judged or betrayed.',
    ' Trust takes time to build but can be lost in a moment, which is why it must be protected with care.',
    ' It grows through consistent actions, truthfulness, and mutual respect.' ,
    'In life, trust gives us confidence to depend on others and also to believe in ourselves.' ,
    'Without trust,relationships become weak and filled with doubt.' ,
    'Therefore, trust is not just a word, but a bond that holds people and the world together.']

speech= random.choice(l1)
print(speech)
start_time=time.time()
user_entry=input('enter:')
end_time=time.time()

total_time=(end_time-start_time)/60
word=0
for i in user_entry:
    if i == ' ':
        word=word+1
typing_speed= word/total_time

original_words = speech.split()
typed_words = user_entry.split()

correct = 0
for i in range(min(len(original_words), len(typed_words))):
    if original_words[i] == typed_words[i]:
        correct += 1

accuracy = (correct / len(original_words)) * 100


print('-'*175)
print('Results')
print(f'The original sentence: {speech}')
print(f'The sentence you typed: {user_entry}')
print(f'Time Taken: {total_time:.2f} minutes')
print(f'Speed in WPM:{typing_speed:.2f} ')
print(f'Accuracy: {accuracy:.2f}%')