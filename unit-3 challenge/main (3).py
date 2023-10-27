def linearSearchProduct(productList, targetProduct):
  indicies = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indicies.append(index)
  return indicies


products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
