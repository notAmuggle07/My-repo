// Sample laptops with prices and configurations
const laptops = [
  {
    id: 1,
    model: 'Standard',
    basePrice: 50000,
    RAM: [
      { size: "8GB", price: 50 },
      { size: "16GB", price: 100 },
      { size: "64GB", price: 400 }
    ],
    storage: [
      { type: "SSD", size: "256GB", price: 100 },
      { type: "SSD", size: "512GB", price: 150 }
    ]
  },
  {
    id: 2,
    model: 'Pro',
    basePrice: 80000,
    RAM: [
      { size: "8GB", price: 150 },
      { size: "16GB", price: 300 },
      { size: "64GB", price: 1200 }
    ],
    storage: [
      { type: "SSD", size: "256GB", price: 200 },
      { type: "SSD", size: "512GB", price: 400 }
    ]
  },
  {
    id: 3,
    model: 'Air',
    basePrice: 95000,
    RAM: [
      { size: "8GB", price: 250 },
      { size: "16GB", price: 500 },
      { size: "64GB", price: 2000 }
    ],
    storage: [
      { type: "SSD", size: "256GB", price: 300 },
      { type: "SSD", size: "512GB", price: 600 }
    ]
  },
];

// Initialize the shopping cart as an array of objects
const cart = [];

// Function to add a laptop configuration to the cart
function addToCart(laptopId, RAMSize, storageSize) {
  // Step 1: Find the laptop with the specified ID in the laptops array
  const laptop = laptops.find((l) => l.id === laptopId);

  // Step 2: Check if the laptop with the specified ID was found
  if (laptop) {
    // Step 3: Find the configuration with matching RAMSize and storageSize
    const config = laptop.RAM.find((ram) => ram.size === RAMSize) && laptop.storage.find((storage) => storage.size === storageSize);

    // Step 4: Check if the matching configuration was found
    if (config) {
      // Step 5: Create a cart item object capturing the laptop and its configuration
      const cartItem = { laptop, config };

      // Step 6: Add the cart item to the cart array
      cart.push(cartItem);

      // Step 7: Display a confirmation message
      console.log(`Added ${laptop.model} to the cart with configuration: RAM ${config.size}GB, Storage ${config.size}GB`);
    } else {
      // Step 4 (Alternative): Handle the case where the specified configuration was not found
      console.log('Configuration not found.');
    }
  } else {
    // Step 2 (Alternative): Handle the case where the specified laptop ID was not found
    console.log('Laptop not found.');
  }
}

// Function to remove an item from the cart based on its index
function removeFromCart(index) {
  if (index >= 0 && index < cart.length) {
    const removedItem = cart.splice(index, 1);
    const { laptop, config } = removedItem[0];
    console.log(`Removed ${laptop.model} with configuration: RAM ${config.size}GB, Storage ${config.size}GB from the cart.`);
  } else {
    console.log('Invalid index. Item not removed from the cart.');
  }
}

// Function to calculate the total price of items in the cart
function calculateTotal() {
  let total = 0;

  for (const cartItem of cart) {
    const { laptop, config } = cartItem;
    const laptopConfig = laptop.RAM.find((ram) => ram.size === config.size) && laptop.storage.find((storage) => storage.size === config.size);

    if (laptopConfig) {
      total += laptopConfig.price;
    }
  }

  // Add the base price of the laptops to the total
  total += cart.reduce((acc, cartItem) => acc + cartItem.laptop.basePrice, 0);

  return total;
}

// Main program loop
while (true) {
  console.log('Options:');
  console.log('1. Add laptop to cart');
  console.log('2. View cart contents');
  console.log('3. Remove laptop from cart');
  console.log('4. Calculate the total price');
  console.log('5. Exit');

  const choice = prompt('Enter your choice: ');

  switch (choice) {
    case '1':
      const laptopId = parseInt(prompt('Enter laptop ID: '));
      const RAMSize = prompt('Enter RAM size (GB): '); // Use string input
      const storageSize = prompt('Enter storage size (GB): '); // Use string input
      addToCart(laptopId, RAMSize, storageSize);
      break;

    case '2':
      console.log('Cart Contents:');
      cart.forEach((cartItem, index) => {
        const { laptop, config } = cartItem;
        console.log(`${index + 1}. ${laptop.model} - Configuration: RAM ${config.size}GB, Storage ${config.size}GB`);
      });
      break;

    case '3':
      const removeIndex = parseInt(prompt('Enter the index of the item to remove: '));
      removeFromCart(removeIndex);
      break;

    case '4':
      const totalPrice = calculateTotal();
      console.log(`Total Price of Items in Cart: $${totalPrice}`);
      break;

    case '5':
      console.log('Thank you for shopping!');
      process.exit(0);
      break;

    default:
      console.log('Invalid choice. Please select a valid option.');
      break;
  }
}