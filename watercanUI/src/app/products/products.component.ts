import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products: any;
  product_details: any;

  constructor(private api: ApiService) {
    this.getProduct();
    this.getProductDetails();
  }

  getProduct = () => {
    this.api.getProduct().subscribe(
      data => {
        this.products = data
      },
      error => {
        console.log(error);
      }
    )
  }

  getProductDetails = () => {
    this.api.getProductDetails().subscribe(
      data => {
        this.product_details = data
      },
      error => {
        console.log(error);
      }
    )
  }

  getSpecificProductDetails = (id) =>{
    var newArray = this.product_details.filter(function (el) {
      return el.product.id == id;
      });
  }

  ngOnInit() {
  }

}
