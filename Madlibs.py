"""
Mad Libs are stories with blank spaces that a reader can fill in with their own words. The result is usually a funny (or strange) story.

Mad Libs require:

Words from the reader (for the blank spaces)
A story to plug the words into
For this project, we'll provide you with the story (feel free to modify it), but it will be up to you to build a program that does the following:

Prompt the user for input
Print the entire Mad Libs story with the user's input in the right places
"""
print "Game Start"
name=raw_input("Enter a name:")
first_adj = raw_input("Enter an adjective: ")
second_adj = raw_input("Enter a second adjective: ")
third_adj = raw_input("Enter one more adjective: ")

first_verb = raw_input("Enter a verb: ")
second_verb = raw_input("Enter a second verb: ")
third_verb = raw_input("Enter one more verb: ")

first_noun = raw_input("Enter a noun: ")
second_noun = raw_input("Enter a second noun: ")
third_noun = raw_input("Enter one more noun: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."
animal = raw_input("Enter an animal: ")
print STORY %(first_adj,name,first_verb,first_noun,second_adj,name,second_verb,second_noun
              ,third_adj,name,third_verb,third_noun,first_adj,name,first_verb,first_noun,second_adj,name,second_verb,second_noun
              ,third_adj,name,third_verb,third_noun,name)
