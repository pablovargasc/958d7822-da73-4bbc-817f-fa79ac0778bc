import fire
import json 

from util import InvestmentProject


class Main(object):
    
    @staticmethod
    def describe_investment(filepath, hurdle_rate=None):
        investment_project = InvestmentProject.from_csv(filepath=filepath, hurdle_rate=hurdle_rate)
        description = investment_project.describe()
        print(json.dumps(description, indent=4))


def plot_investment(filepath, save="", show=False):
    # TODO: implement plot_investment method
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111)

    self.figure = self.ax.plot([flow.t for flow in self.cashflows], [flow.amount for flow in self.cashflows])
    if show:
        plt.show()
    if kwargs.get('name'):
        plt.title('cashflows')
        plt.ylabel('amount')
        plt.xlabel('t')
        self.fig.savefig(kwargs.get('name'))


if __name__ == "__main__":
    fire.Fire(Main)
