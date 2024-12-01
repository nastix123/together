enum Role { UNKNOWN, VOLUNTEER, NEEDY }

class User {
  final String id;
  final Role role;
  final String name;
  final String surname;
  final String city;
  final String email;

  User({
    required this.id,
    required this.role,
    required this.name,
    required this.surname,
    required this.city,
    required this.email,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'role': role.name,
      'name': name,
      'surname': surname,
      'city': city,
      'email': email,
    };
  }


  factory User.fromMap(Map<String, dynamic> map) {
    return User(
      id: map['id'] as String,
      role: Role.values.firstWhere((e) => e.name == map['role'], orElse: () => Role.UNKNOWN),
      name: map['name'] as String,
      surname: map['surname'] as String,
      city: map['city'] as String,
      email: map['email'] as String,
    );
  }
}
