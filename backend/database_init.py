import sqlite3

file = "backend/tweets.db"

try:
  conn = sqlite3.connect(file)
  print("Database Sqlite3.db formed.")
except:
  print("Database Sqlite3.db not formed.")