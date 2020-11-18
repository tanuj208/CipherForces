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
import classnames from "classnames";
import { Link } from "react-router-dom";

// reactstrap components
import {
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardImg,
  CardTitle,
  Label,
  FormGroup,
  Form,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Container,
  Row,
  Col,
  Table
} from "reactstrap";

// core components
import IndexNavbar from "components/Navbars/IndexNavbar.js";
import Footer from "components/Footer/Footer.js";

class Algorithms extends React.Component {
  state = {
    squares1to6: "",
    squares7and8: "",
    c1: 0,
    c2: 0,
    c3: 0,
    c4: 0
  };
  componentDidMount() {
    console.log("done");
    document.body.classList.toggle("register-page");
    document.documentElement.addEventListener("mousemove", this.followCursor);

    var url1 = new URL('http://localhost:5000/get_level_count')
    url1.searchParams.append('level', 1)
    fetch(url1)
    .then(res => res.text())
    .then(result => {
        this.setState({
          c1 : result
        });
    });

    var url2 = new URL('http://localhost:5000/get_level_count')
    url2.searchParams.append('level', 2)
    fetch(url2)
    .then(res => res.json())
    .then(result => {
        this.setState({
          c2 : result
        });
    });

    var url3 = new URL('http://localhost:5000/get_level_count')
    url3.searchParams.append('level', 3)
    fetch(url3)
    .then(res => res.json())
    .then(result => {
        this.setState({
          c3 : result
        });
    });

    var url4 = new URL('http://localhost:5000/get_level_count')
    url4.searchParams.append('level', 4)
    fetch(url4)
    .then(res => res.json())
    .then(result => {
        this.setState({
          c4 : result
        });
    });

    
    fetch('http://localhost:5000/algorithms')
    .then(res => res.json())
    .then(result => {
        this.setState({
          data : JSON.parse(JSON.stringify(result))
        }); 
    });
    console.log(this.state.data);
  }
  componentWillUnmount() {
    document.body.classList.toggle("register-page");
    document.documentElement.removeEventListener(
      "mousemove",
      this.followCursor
    );
  }
  followCursor = event => {
    let posX = event.clientX - window.innerWidth / 2;
    let posY = event.clientY - window.innerWidth / 6;
    this.setState({
      squares1to6:
        "perspective(500px) rotateY(" +
        posX * 0.05 +
        "deg) rotateX(" +
        posY * -0.05 +
        "deg)",
      squares7and8:
        "perspective(500px) rotateY(" +
        posX * 0.02 +
        "deg) rotateX(" +
        posY * -0.02 +
        "deg)"
    });
  };
  render() {
    return (
      <>
        <IndexNavbar />
        <div className="wrapper">
          <div className="page-header">
            <div className="page-header-image" />
            <div className="content">
              <Container>
                <Row>
                  <Col className="offset-lg-0 offset-md-0" lg="12" md="12">
                    <div
                      className="square square-7"
                      id="square7"
                      style={{ transform: this.state.squares7and8 }}
                    />
                    <div
                      className="square square-8"
                      id="square8"
                      style={{ transform: this.state.squares7and8 }}
                    />
                      <h2 className="title">Test Schemes</h2>
                    <Card className="card-register">
                      <CardBody>
                        <Table responsive>
                          <thead>
                              <tr>
                                  
                                  <th className="text-center">Level of algorithms</th>
                                  <th className="text-center">Number of Algorithms</th>
                                  <th className="text-center">Solve</th>
                              </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td className="text-center">Ancient Cipher</td>
                              <td className="text-center">{this.state.c1}</td>
                              <td className="text-center">
                                  <Button className="btn-icon btn-simple" color="info" size="sm" tag={Link} to={`/algo/${1}`}>
                                      <i className="fa fa-user"></i>
                                  </Button>{` `}
                               </td>
                            </tr>
                            <tr>
                              <td className="text-center">Public Key</td>
                              <td className="text-center">{this.state.c2}</td>
                              <td className="text-center">
                                  <Button className="btn-icon btn-simple" color="info" size="sm" tag={Link} to={`/algo/${2}`}>
                                      <i className="fa fa-user"></i>
                                  </Button>{` `}
                               </td>
                            </tr>
                            <tr>
                              <td className="text-center">Hashing</td>
                              <td className="text-center">{this.state.c3}</td>
                              <td className="text-center">
                                  <Button className="btn-icon btn-simple" color="info" size="sm" tag={Link} to={`/algo/${3}`}>
                                      <i className="fa fa-user"></i>
                                  </Button>{` `}
                               </td>
                            </tr>
                            <tr>
                              <td className="text-center">Miscellaneous</td>
                              <td className="text-center">{this.state.c4}</td>
                              <td className="text-center">
                                  <Button className="btn-icon btn-simple" color="info" size="sm" tag={Link} to={`/algo/${4}`}>
                                      <i className="fa fa-user"></i>
                                  </Button>{` `}
                               </td>
                            </tr>
                          </tbody>
                      </Table>
                      </CardBody>
                      <CardFooter>
                        <Button className="btn-round" color="primary" size="lg" tag={Link} to="/add-scheme">
                          Add Algorithm
                          </Button>
                        
                      </CardFooter>
                    </Card>
                  </Col>
                </Row>
                <div className="register-bg" />
                <div
                  className="square square-1"
                  id="square1"
                  style={{ transform: this.state.squares1to6 }}
                />
                <div
                  className="square square-2"
                  id="square2"
                  style={{ transform: this.state.squares1to6 }}
                />
                <div
                  className="square square-3"
                  id="square3"
                  style={{ transform: this.state.squares1to6 }}
                />
                <div
                  className="square square-4"
                  id="square4"
                  style={{ transform: this.state.squares1to6 }}
                />
                <div
                  className="square square-5"
                  id="square5"
                  style={{ transform: this.state.squares1to6 }}
                />
                <div
                  className="square square-6"
                  id="square6"
                  style={{ transform: this.state.squares1to6 }}
                />
              </Container>
            </div>
          </div>
          <Footer />
        </div>
      </>
    );
  }
}

export default Algorithms;
