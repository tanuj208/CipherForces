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
  FormText,
} from "reactstrap";

// core components
import IndexNavbar from "components/Navbars/IndexNavbar.js";
import Footer from "components/Footer/Footer.js";

class AddScheme extends React.Component {
  state = {};
  componentDidMount() {
    document.body.classList.toggle("index-page");
  }
  componentWillUnmount() {
    document.body.classList.toggle("index-page");
  }
  render() {
    return (
      <>
        <IndexNavbar />
        <div className="wrapper">
            <div className="section section-signup">
            <Container>
              <div className="squares square-1" />
              <div className="squares square-2" />
              <div className="squares square-3" />
              <div className="squares square-4" />
              <Row className="row-grid justify-content-between align-items-center">
                <Col className="mb-lg-auto" lg="8">
                  <h2 className="title">Add Scheme</h2>
                  <Card className="card-register">
                    <CardBody>
                      <Form className="form">
                        <FormGroup>
                          <Label for="nameField">Name</Label>
                          <Input
                            type="text"
                            name="name"
                            id="nameField"
                            placeholder="Name your Algorithm"
                          />
                        </FormGroup>
                        <FormGroup>
                          <Label for="typeField">Type</Label>
                          <Input
                            type="text"
                            name="type"
                            id="typeField"
                            placeholder="Specify Algorithm Type"
                          />
                        </FormGroup>

                        <FormGroup>
                          <Label for="descriptionField">Description</Label>
                          <Input
                            type="textarea"
                            name="description"
                            id="descriptionField"
                          />
                        </FormGroup>

                        <FormGroup>
                          <Label for="challengeField">Challenge</Label>
                          <Input
                            type="textarea"
                            name="challenge"
                            id="challengeField"
                          />
                        </FormGroup>

                        <FormGroup>
                          <Label for="hintField">Hint</Label>
                          <Input
                            type="textarea"
                            name="hint"
                            id="hintField"
                          />
                        </FormGroup>
                        
                        <FormGroup>
                          <Label for="plaintextField">Plaintext</Label>
                          <Input
                            type="text"
                            name="plaintext"
                            id="plaintextField"
                            placeholder="Enter Plaintext to be found"
                          />
                        </FormGroup>
                        <FormGroup>
                          <Label for="ciphertextField">Ciphertext</Label>
                          <Input
                            type="text"
                            name="ciphertext"
                            id="ciphertextField"
                            placeholder="Enter Ciphertext for challenge"
                          />
                        </FormGroup>

                        <FormGroup>
                          <Label for="fileField">
                            <Button
                              className="btn-icon btn-round"
                              color="primary"
                              type="button"
                            >
                              <i className="tim-icons icon-cloud-upload-94" />
                            </Button>
                          </Label>
                          <Input
                            type="file"
                            name="file"
                            id="fileField"
                          />
                        </FormGroup>

                      <Button className="btn-round" color="primary" size="lg">
                        Add
                      </Button>
                      </Form>
                    </CardBody>
                  </Card>
                </Col>
                <Col lg="4">
                  <h3 className="display-3 text-white">
                    The Algorithm Format should{" "}
                    <span className="text-white">be as defined below</span>
                  </h3>
                  <p className="text-white mb-3">
                    The Design System comes with four pre-built pages to help you
                    get started faster. You can change the text and images and
                    you're good to go. More importantly, looking at them will give
                    you a picture of what you can built with this powerful Bootstrap
                    4 Design System.
                  </p>
                </Col>
                
              </Row>
            </Container>
            </div>
          <Footer />
        </div>
      </>
    );
  }
}

export default AddScheme;
