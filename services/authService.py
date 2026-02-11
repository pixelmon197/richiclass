from repository.userRepository import UserRepository

class authService:
    @staticmethod
    def register(username,email,password):
        user = UserRepository.create(username,email,password)
        return user
    
    @staticmethod
    def find_by_id(id):
        return UserRepository.find_by_id(id)