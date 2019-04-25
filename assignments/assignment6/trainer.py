import time

from torch.autograd.variable import Variable


class Trainer:
    def __init__(self, net, N_seconds=1, DEBUG=False):
        self.net = net
        self.N_seconds = N_seconds
        self.DEBUG = DEBUG
        self.losses = []

    def get_losses(self):
        return self.losses
    
    def get_options(self):
        raise NotImplemented
    
    def get_data(self):
        raise NotImplemented
    
    def print_debug_info(self, X, y):
        print(X, y)
    
    def print_prediction(self, X, y, yhat):
        print('example prediction:', y, yhat)
    
    def print_log(self, epoch, batch, loss):
        print('[%d, %5d] loss: %.3f' % (epoch, batch, loss))        
    
    def train_net(self, n_epochs, n_batches):
        """
        Этот метод тренирует нейросеть в течение n_epochs эпох 
        из n мини-батчей, а также выводит каждые N секунд
        средний лосс (используйте метод self.print_log для вывода )
        Также каждый шаг полученный лосс добавляется в список self.losses.
        Реализуйте этот метод.
        """
        loss_criterion, optimizer = self.get_options()
    
        ###
        # TODO: YOUR CODE
        # Чтобы получить данные:
        # X, y = self.get_data()
        # inputs, labels = Variable(X), Variable(y)
        # 
        # Чтобы определить, надо ли выводить результаты вычислений (прошло ли N секунд):
        # last_time = 0
        # И потом в цикле:
        # t = time.time()
        #        if t > last_time + self.N_seconds:
        #            last_time = t
        #            will_print = True
        #
        # Чтобы применить лосс: 
        # loss = loss_criterion(outputs, labels)
        # loss.backward()
        # optimizer.step()
        
        # Чтобы взять число, значение функции потерь:
        # l = loss.data[0]
      
        #END CODE    
        ###