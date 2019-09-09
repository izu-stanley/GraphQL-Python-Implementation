import graphene
import requests

def getPrice():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(url).json()
    data = data['bpi']['USD']['rate_float']
    return data

class GetArgs(graphene.InputObjectType):
    margin = graphene.Float(required=True)
    rate = graphene.Float(required=True)
    type = graphene.Float(required=True)
    @property
    def calculatePrice(self):
        if type == 1:
            self.usd = getPrice()
            self.usd = self.usd + ((self.margin/100) * self.usd) 
            price = self.usd * self.exchangeRate
            return price
        elif type == 2:
            self.usd = getPrice()
            self.usd = self.usd - ((self.margin/100) * self.usd)
            price = self.usd * self.exchangeRate
            return price



class calcPrice(graphene.ObjectType):
    calculatePrice = graphene.String()
    


class Query(graphene.ObjectType):
    address = graphene.Field(calcPrice, pars=GetArgs(required=True))

    def resolve_address(self, info, pars):
        return calcPrice(calculatePrice=pars.calculatePrice)




schema = graphene.Schema(query=Query)
query = """
    query something{
      price(pars: {margin:0.2, rate:360,type:1}) {
        calculatePrice
      }
    }
"""





if __name__ == "__main__":
    result = schema.execute(query)
    print(result.data)