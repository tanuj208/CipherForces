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
    data : [] 
  };
  componentDidMount() {
    console.log("done");
    document.body.classList.toggle("register-page");
    document.documentElement.addEventListener("mousemove", this.followCursor);
    fetch('http://localhost:5000')
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
                                  <th className="text-center">#</th>
                                  <th>Name</th>
                                  <th>Type</th>
                                  <th className="text-center">Attempts</th>
                                  <th className="text-center">Success</th>
                                  <th className="text-center">Actions</th>
                              </tr>
                          </thead>
                          <tbody>
                            {
                                this.state.data.map( (row, index) => {
                                  return(
                                    <tr key = {index}>
                                      <td className="text-center">{row.id}</td>
                                      <td>{row.name}</td>
                                      <td>{row.type}</td>
                                      <td className="text-center">{row.attempts}</td>
                                      <td className="text-center">{row.success}</td>
                                      <td className="text-center">
                                      <Button className="btn-icon btn-simple" color="info" size="sm">
                                          <i className="fa fa-user"></i>
                                      </Button>{` `}
                                      <Button className="btn-icon btn-simple" color="success" size="sm">
                                          <i className="fa fa-edit"></i>
                                      </Button>{` `}
                                      <Button className="btn-icon btn-simple" color="danger" size="sm">
                                          <i className="fa fa-times" />
                                      </Button>{` `}
                                      </td>
                                    </tr>
                                  )
                                })
                            }
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
