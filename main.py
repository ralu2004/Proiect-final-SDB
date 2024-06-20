from repository.repository import Repository
from service.admin_service import AdminService
from service.client_service import ClientService
from service.promotion_service import PromotionService
from validator.product_validator import ProductValidator
from ui.console import Console

product_repository = Repository()
promotion_repository = Repository()

admin_service = AdminService(product_repository)
client_service = ClientService(product_repository)
promotion_service = PromotionService(product_repository, promotion_repository)

product_validator = ProductValidator()

ui = Console(client_service, admin_service, promotion_service, product_validator)

ui.run()

