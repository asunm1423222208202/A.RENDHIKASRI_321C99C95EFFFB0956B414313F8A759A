"""write a function called linear_search_product that takes the list of products and a target product name as input."""

def linearSearchProduct(productlist, targetProduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == targetProduct:
      indices.append(index)

  return indices


#Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2="phone"
result = linearSearchProduct(products, target)
print(result)