/*!

=========================================================
* BLK Design System React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/blk-design-system-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/blk-design-system-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";

// reactstrap components
import { Button, Container } from "reactstrap";
import { Link } from "react-router-dom";

class PageHeader extends React.Component {
  render() {
    return (
      <div className="page-header header-filter">
        <div className="squares square1" />
        <div className="squares square2" />
        <div className="squares square3" />
        <div className="squares square4" />
        <div className="squares square5" />
        <div className="squares square6" />
        <div className="squares square7" />
        <Container>
          <div className="content-center brand">
            <h1 className="h1-seo">Breaking In!</h1>
            <h3 className="d-none d-sm-block">
              A Crowsourced learning Platform for Security Schemes
            </h3>
            <Button
                className="btn-simple btn-round"
                color="primary"
                type="button"
                tag={Link} 
                to="/algorithms"
              >
                Get Started
              </Button>
          </div>
        </Container>
      </div>
    );
  }
}

export default PageHeader;
