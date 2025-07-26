from abc import ABC,abstractmethod

class DeliveryAgent(ABC):

    def __init__(self, order, delivery_type, delivery_id):
        self.order = order
        self.delivery_type = delivery_type
        self.delivery_id = delivery_id

    @abstractmethod
    def deliver_order(order):
        pass
    
class Person:

    def __init__(self, name, agent_id):
        self.name = name
        self.agent_id = agent_id

class HumanRider(Person, DeliveryAgent):

    def __init__(self,name, agent_id, order, deliver_type, delivery_id):
        Person.__init__(self, name, agent_id)
        DeliveryAgent.__init__(self, order, deliver_type, delivery_id)

    def deliver_order(self,order):
        return f"Order {order.order_id} is being delivered by {self.name} (Human Rider). Delivery ID: {self.delivery_id}"
    

class AutoBot(DeliveryAgent):
    
    def __init__(self, order, delivery_type, delivery_id, bot_id):
        super().__init__( order, delivery_type, delivery_id)
        self.bot_id = bot_id

    def deliver_order(self, order):
        return f"Order {order.order_id} is being delivered by {self.bot_id} (AutoBot). Delivery ID: {self.delivery_id}"