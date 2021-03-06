import React from 'react' 
import { Link } from 'react-router-dom'
import { PageHeader, Alert, Row, Col, Button } from 'antd'
import ListLieuConsult from '../containers/ListLieuConsult'
import DetailLieuConsult from '../containers/DetailLieuConsult'
import { PlusCircleOutlined } from '@ant-design/icons'


class LieuConsult extends React.Component {
    render(){
        const description = "Renseignez er gérez toutes les informations relatives à votre lieu de consultation. Ces derniéres permettent à vos patients de vous trouver plus simplement."
        return ( 
            <PageHeader
            title="Lieu de consultation"
            extra={[
                <Link to="create-lieu-consult" key="1">
                    <Button> Ajouter un lieu de consultation<PlusCircleOutlined/></Button>
                </Link>,
                
            ]}
            >
                <Alert type="info" message ={description} />
            
                <Row>
                    <Col span={8}>
                        <ListLieuConsult/>
                    </Col>

                    <Col span={16}>
                        <DetailLieuConsult/>
                    </Col>
                </Row>
                
            </PageHeader>
        )
    }
}

export default LieuConsult