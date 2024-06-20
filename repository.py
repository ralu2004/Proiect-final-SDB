from exceptions.exceptions import NotFoundException, DuplicateException


class Repository:
    def __init__(self):
        self.__entities_list = []

    def __find_entity_position(self, entity):
        """
        Given an entity it finds it's position in the list of entities
        :param entity: Entity to be found
        :return: The position of the entity if it is found, otherwise, None
        """
        for index in range(len(self.__entities_list)):
            if self.__entities_list[index] == entity:
                return index
        return None

    def add(self, new_entity):
        """
        Given a new entity, it adds it to the list, if it doesn't already exist
        :param new_entity: Entity to be added
        :return:
        """
        if self.__find_entity_position(new_entity) is not None:
            raise DuplicateException(new_entity)
        self.__entities_list.append(new_entity)

    def delete(self, entity):
        """
        Deletes a given entity
        :param entity: Entity to be deleted
        :return:
        """
        entity_position = self.__find_entity_position(entity)
        if entity_position is None:
            raise NotFoundException(entity)
        del self.__entities_list[entity_position]

    def get_all_entities(self):
        """
        Return the list of all entities
        :return: All the entities (list)
        """
        return self.__entities_list



