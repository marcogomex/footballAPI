import pytest

from footballAPI import APIFootball

from footballAPI.exceptions import InvalidStatusCode, InvalidParams

class TestAPIFootball:
	def setup(self):
		self.api = APIFootball()
		self.endpoint1 = "status"
		self.endpoint2 = "countries"

	def test_check_200_status_code(self):
		assert self.api._check_status_code(200) is None

	def test_check_not_200_status_code(self):
		with pytest.raises(InvalidStatusCode):
			self.api._check_status_code(100)

	def test_get_non_dict_params_erros(self):
		with pytest.raises(InvalidParams):
			self.api._get(
				endpoint=self.endpoint1,
				dryrun=True,
				params="these are bad params"
				)

	def test_dryrun_get_returns_none(self):
		assert self.api._get(endpoint=self.endpoint1, dryrun=True) is None