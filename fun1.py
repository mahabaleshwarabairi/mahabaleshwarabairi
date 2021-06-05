# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:06:29 2020

@author: Mahabaleshwara.Bairi
"""

def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

def my_function0(fname, lname):
  print(fname + " " + lname)

my_function0("Emil", "Refsnes")


def my_function(*kids):
  print("The youngest child is " + kids[0]+" "+kids[1]+" "+kids[2])

my_function("Emil", "Tobias", "Linus")


print ("If the number of keyword arguments is unknown, add a double ** before the parameter name:")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)