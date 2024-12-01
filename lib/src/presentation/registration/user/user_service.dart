import 'package:shared_preferences/shared_preferences.dart';
import 'user.dart';
import 'dart:convert';

class UserService {
  static const _userKey = 'user_data';


   Future<void> saveUser(User user) async {
    final prefs = await SharedPreferences.getInstance();
    final String userJson = jsonEncode(user.toMap());
    await prefs.setString(_userKey, userJson);
  }

  Future<User?> getUser() async {
    final prefs = await SharedPreferences.getInstance();
    final userData = prefs.getString(_userKey);
    if (userData == null) return null;

    final Map<String, dynamic> userMap = jsonDecode(userData); 
    return User.fromMap(userMap);
  }

 Future<void> clearUser() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_userKey);
  }
  
}
