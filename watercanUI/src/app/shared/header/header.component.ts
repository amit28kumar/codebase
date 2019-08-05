import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';
import { Globals } from '../../globals';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  product_details: any;
  filtered_product: any;
  product_id: any;

  constructor(private api: ApiService, private global: Globals) {
    this.getProductDetails();
  }

  getProductDetails = () => {
    this.api.getProductDetails(this.product_id).subscribe(
      data => {
        this.product_details = data;
      },
      error => {
        console.log(error);
      }
    )
  }

  setSearchFlag(){
    if(this.global.searchFlag){
      this.global.searchFlag = !this.global.searchFlag;
    }
  }

  searchProductDetails(event){
    this.global.searchKey = event.target.value ;
    this.global.searchFlag = true;
  }

  ngOnInit() {
  }

}
