from pages.choose_vehicle import ChooseVehicle, VehicleType
import pytest


@pytest.fixture
def vehicle_page(driver):
    cv = ChooseVehicle(driver)
    return cv


class TestVehicle:

    @pytest.mark.parametrize("vehicle, brand, model, type, full_name",
                             [(VehicleType.car, "Audi", "A3 (8V1, 8VK)", "2.0 TDI", "Audi A3 (8V1, 8VK) 2.0 TDI"),
                              (VehicleType.truck, "Ford", "Cargo", "1013", "Ford Cargo 1013, Leistung: 128 PS/94 kW"),
                                 (VehicleType.motorbike, "Honda", "Forza", "250EX", "Honda Forza 250EX"),
                             (VehicleType.farm, "Zetor", "4000", "4320", "Zetor 4000 4320"),
                              (VehicleType.boat, "Colt", "COLT", "5.0 HP", "Colt COLT 5.0 HP")])
    def test_choose_vehicle(self, vehicle_page, vehicle, brand, model, type, full_name):
        vehicle_page.switch_tab(vehicle)
        vehicle_page.select_brand_by_text(brand)
        vehicle_page.select_model_by_text(model)
        vehicle_page.select_type_by_text(type)
        vehicle_page.click_save_vehicle()
        name_of_selected_car = vehicle_page.get_chosen_vehicle_name()
        assert full_name == name_of_selected_car
