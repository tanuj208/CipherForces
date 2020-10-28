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

class SolveChallenge extends React.Component {
  state = {
    data : {}
  };
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.onChange = this.onChange.bind(this); 
  }
  handleSubmit() {
    var url = new URL("http://localhost:5000/solve-challenge");
    const data = new FormData();
    Object.keys(this.state.data).forEach(key => data.append(key, this.state.data[key]))
    const requestOptions = {
      method: 'POST',
      // headers: {'Content-Type': 'application/json'},
      body: data,
    };
    // for(var key of requestOptions['body'].entries())
    // {
    //   console.log(key[0], "F", key[1]);
    // }
    console.log(requestOptions);
    fetch(url, requestOptions)
    .then(response => {
        console.log(response);
        // for(var key in response){
        //   console.log(key, response[key])
        // }
    });
  }
  onChange(e) {
    
    if(e.target.id === 'plaintextField') {
      let newState = Object.assign({}, this.state.data);
      newState['plaintext'] = e.target.value;
      this.setState({data : newState});
    }
    else if(e.target.id === 'ciphertextField') {
      let newState = Object.assign({}, this.state.data);
      newState['ciphertext'] = e.target.value;
      this.setState({data : newState});
    }
  }
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
                  <h2 className="title">Solve Challenge</h2>
                  <Card className="card-register">
                    <CardBody>
                      <Form className="form" onSubmit = {this.handleSubmit}>
                        <FormGroup>
                          <Label for="ciphertextField">Ciphertext</Label>
                          <Input
                            onChange={this.onChange}
                            type="text"
                            name="ciphertext"
                            id="ciphertextField"
                            placeholder="Enter the ciphertext"
                            required
                          />
                        </FormGroup>
                        <FormGroup>
                          <Label for="plaintextField">Plaintext</Label>
                          <Input
                            onChange={this.onChange}
                            type="text"
                            name="plaintext"
                            id="plaintextField"
                            placeholder="Enter the decrypted plaintext"
                            required
                          />
                        </FormGroup>
                       

                       
                      <Button className="btn-round" color="primary" size="lg">
                        Submit
                      </Button>
                      </Form>
                    </CardBody>
                  </Card>
                </Col>
                <Col lg="4">
                  <h3 className="display-3 text-white">
                    Enter the Plain Text{" "}
                    <span className="text-white">and Cipher Text</span>
                  </h3>
                  
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

export default SolveChallenge;