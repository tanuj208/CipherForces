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
    data : {},
    cipher : "None",
    plain : "None",
    hintflag : 0,
    status : "Unsolved"
  };
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.onChange = this.onChange.bind(this); 
  }
  componentDidMount() {
    var url = new URL('http://localhost:5000/get_algo')
    var id_val = this.props.match.params.id
    console.log("aaaaaaaaaaaaaaaaa");
    console.log(id_val);
    url.searchParams.append('id', id_val)
    fetch(url)
    .then(res => res.json())
    .then(result => {
        this.setState({
          data : JSON.parse(JSON.stringify(result))
        });
    });
    console.log(this.state.data);
    document.body.classList.toggle("index-page");
  }
  handleHint(event) {
    event.preventDefault();
    this.setState({
      hintflag : !this.state.hintflag
    });
  }
  handleSolve(event) {
    event.preventDefault();
    if(this.state.data.providedSolution == this.state.data.solution)
    {
      this.setState({
        status : "SUCCESS"
      });
    }
    else
    {
      this.setState({
        status : "WRONG ANSWER"
      });
    }
  }
  handleSubmit(event) {
    event.preventDefault();
    var url = new URL("http://localhost:5000/encrypt");
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
    // var response = "FOLAAAA"
    // console.log(requestOptions);
    // fetch(url, requestOptions)
    // .then(response => {
    //     console.log("geeting");
    //     console.log(response);
    //     for(var key in response){
    //       console.log(key, response[key])
    //     }
    // });

    fetch(url, requestOptions)
    .then(res => res.json())
    .then(res => {
        console.log(res)
        this.setState({
          cipher : res["ciphertext"]
        });
    });
    // this.state.data = response;
  }

  handleSubmit2(event) {
    event.preventDefault();
    var url = new URL("http://localhost:5000/decrypt");
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
    // var response = "FOLAAAA"
    // console.log(requestOptions);
    // fetch(url, requestOptions)
    // .then(response => {
    //     console.log("geeting");
    //     console.log(response);
    //     for(var key in response){
    //       console.log(key, response[key])
    //     }
    // });

    fetch(url, requestOptions)
    .then(res => res.json())
    .then(res => {
        console.log(res)
        this.setState({
          plain : res["plaintext"]
        });
    });
    // this.state.data = response;
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
    else if(e.target.id === 'solutionField') {
      let newState = Object.assign({}, this.state.data);
      newState['providedSolution'] = e.target.value;
      this.setState({data : newState});
    }
  }
  componentWillUnmount() {
    document.body.classList.toggle("index-page");
  }
  render() {
    console.log(this.state);
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
                  <h2 className="title">{this.state.data.name}</h2>
                  <Card>
                  <CardBody>
                  <Label> Description </Label>
                  <div>
                  {this.state.data.description}
                  </div>
                  </CardBody>
                  </Card>
                  <Card>
                  <CardBody>
                  <Label> Hint </Label>
                  <div>
                  <Button className="btn-icon" color="primary" size="sm" onClick={this.handleHint.bind(this)}>
                  :)
                  </Button>
                  {this.state.hintflag == 1 && <div>
                  {this.state.data.hint}
                  aa
                  {this.state.data.allow_encrypt}
                  </div>}
                  </div>
                  </CardBody>
                  </Card>
                  <Card>
                  <CardBody>
                  <Label> Challenge </Label>
                  <div>
                  {this.state.data.challenge}
                  </div>
                  </CardBody>
                  </Card>
                  {this.state.data.allow_encrypt == "yes" &&
                  <Card className="card-register">
                    <CardBody>
                      <Form className="form" onSubmit = {this.handleSubmit}>
                        <FormGroup>
                          <Label for="ciphertextField">Plaintext</Label>
                          <Input
                            onChange={this.onChange}
                            type="text"
                            name="plaintext"
                            id="plaintextField"
                            placeholder="Enter plain text"
                            required
                          />
                        </FormGroup>
                      
      

                       
                      <Button className="btn-round" color="primary" size="lg">
                        Encrypt
                      </Button>

                      </Form>
                    </CardBody>
                  </Card>}
                  {this.state.data.allow_encrypt == "yes" && <Card>
                  <CardBody>
                      <div> Corresponding Cipher Text :- {this.state.cipher} </div>
                  </CardBody>
                  </Card>}

                  {this.state.data.allow_decrypt == "yes" &&
                  <Card className="card-register">
                    <CardBody>
                      <Form className="form" onSubmit = {this.handleSubmit}>
                        <FormGroup>
                          <Label for="plaintextField">CipherText</Label>
                          <Input
                            onChange={this.onChange}
                            type="text"
                            name="ciphertext"
                            id="ciphertextField"
                            placeholder="Enter cipher text"
                            required
                          />
                        </FormGroup>
                      
      

                       
                      <Button className="btn-round" color="primary" size="lg">
                        Decrypt
                      </Button>

                      </Form>
                    </CardBody>
                  </Card>}
                  {this.state.data.allow_decrypt == "yes" && <Card>
                  <CardBody>
                      <div> Corresponding Plain Text :- {this.state.plain} </div>
                  </CardBody>
                  </Card>}


                  <Card>
                  <CardBody>
                    <Form className="form" onSubmit = {this.handleSolve.bind(this)}>
                        <FormGroup>
                          <Label for="answerField">Your Answer</Label>
                          <Input
                            onChange={this.onChange}
                            type="text"
                            name="solution"
                            id="solutionField"
                            placeholder="Enter solution"
                            required
                          />
                        </FormGroup>
                        <Button className="btn-round" color="primary" size="lg">
                        Submit Answer
                      </Button>
                  </Form>
                  </CardBody>
                  </Card>
                  <Card>
                  <CardBody>
                      <div> Verdict :- {this.state.status} </div>
                  </CardBody>
                  </Card>
                </Col>
                <Col lg="4">  
                  <h3 className="display-3 text-white">
                    Algorithm Details 
                    <span className="text-white"> and SIA dialog box</span>
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