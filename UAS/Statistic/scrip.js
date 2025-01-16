document.getElementById('orderForm').addEventListener('submit', function(event) {
  event.preventDefault(); 
  
  const name = document.getElementById('name').value;
  const product = document.getElementById('product').value;

  alert(`Terima kasih, ${name}! Anda telah memesan produk: ${product}.`);

  document.getElementById('name').value = '';
  document.getElementById('product').value = '';
});
