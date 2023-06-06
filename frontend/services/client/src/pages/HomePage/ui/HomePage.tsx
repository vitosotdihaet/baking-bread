import {
    FC,
} from 'react';
import { useGetGoodsWithType } from 'widgets/Navbar/api/goodsTypeApi';
import { Page } from 'widgets/Page/Page';
import { GoodListWithType } from 'features/goodListWithType';
import { classNames } from 'shared/lib/classNames/classNames';
import { Column } from 'shared/ui/Stack';

interface HomePageProps {
    className?: string;
}

const HomePage: FC<HomePageProps> = (props) => {
    const { className } = props;
    const { data } = useGetGoodsWithType();

    if (!data) {
        return null;
    }

    return (
        <>
            <Page className={classNames('', {}, [className])}>
                <Column gap='32'>
                    {data.map((goodType) => (
                        <GoodListWithType
                            key={goodType.id}
                            goodType={goodType}
                        />
                    ))}
                </Column>
            </Page>
        </>
    );
};

export default HomePage;
