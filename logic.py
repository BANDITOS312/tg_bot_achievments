import sqlite3
import random

DATABASE = "achievments.db"

class DB_Manager:
    def __init__(self, db_path=DATABASE):
        self.db_path = db_path

    def _execute_query(self, query, params=()):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_description_name(self, achievement_name):
        query = "SELECT description FROM Terraria WHERE Achievement = ?"
        result = self._execute_query(query, (achievement_name,))
        return result[0][0] if result else None

    def get_NeedToDo_name(self, achievement_name):
        query = "SELECT NeedToDo FROM Terraria WHERE Achievement = ?"
        result = self._execute_query(query, (achievement_name,))
        return result[0][0] if result else None

    def get_name(self, achievementID):
        query = "SELECT Achievement FROM Terraria WHERE AchievementID = ?"
        result = self._execute_query(query, (achievementID,))
        return result[0][0] if result else None

    def get_description_id(self, achievementID):
        query = "SELECT description FROM Terraria WHERE AchievementID = ?"
        result = self._execute_query(query, (achievementID,))
        return result[0][0] if result else None

    def get_NeedToDo_id(self, achievementID):
        query = "SELECT NeedToDo FROM Terraria WHERE AchievementID = ?"
        result = self._execute_query(query, (achievementID,))
        return result[0][0] if result else None

    def get_count(self):
        query = "SELECT count(AchievementID) FROM Terraria"
        result = self._execute_query(query)
        return result[0][0] if result else 0

    def get_random_achievement(self):
        count = self.get_count()
        if count == 0:
            return None  
        id = random.randint(1, count)

        name_achievement = self.get_name(id)
        description = self.get_description_id(id)
        NeedToDo = self.get_NeedToDo_id(id)

        return name_achievement, description, NeedToDo

