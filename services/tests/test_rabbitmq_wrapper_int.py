from services.rabbitmq_wrapper import RabbitMqWrapper
import yaml

def test_given_validRabbitConfigurations_when_connectCalled_then_expectSuccessfulConnection(configs):
    wrapper = RabbitMqWrapper(configs["queue"])
    cp = wrapper.get_connection_params()
    opened = cp.is_open
    wrapper.close_connection()
    assert opened