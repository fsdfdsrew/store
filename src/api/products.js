import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getProducts = async () => {
  const response = await axios.get(`${API_URL}/products`);
  console.log(response.data);
  return response.data;
};

export const createProduct = async (product) => {
  const response = await axios.post(`${API_URL}/products`, product);
  return response.data;
};
