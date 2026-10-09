class UserService:

    @staticmethod
    def get_profile(user):

        return {
            "id": user.id,
            "uuid": str(user.uuid),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "email": user.email,
            "role": user.role,
        }