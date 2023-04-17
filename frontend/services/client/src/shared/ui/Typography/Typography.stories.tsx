import { ComponentStory, ComponentMeta } from '@storybook/react';
import { Typography } from './Typography';

export default {
    title: 'shared/Typography',
    component: Typography,
    args: {
        children: 'Typography',
    },
} as ComponentMeta<typeof Typography>;

const Template: ComponentStory<typeof Typography> = (args) => <Typography {...args} />;

export const Primary = Template.bind({});
Primary.args = {
    color: 'primary',
};

export const Secondary = Template.bind({});
Secondary.args = {
    color: 'secondary',
};

export const Accent = Template.bind({});
Accent.args = {
    color: 'accent',
};

export const Soft = Template.bind({});
Soft.args = {
    color: 'soft',
};

export const Disabled = Template.bind({});
Disabled.args = {
    color: 'disabled',
};

export const AlignLeft = Template.bind({});
AlignLeft.args = {
    align: 'left',
};

export const AlignCenter = Template.bind({});
AlignCenter.args = {
    align: 'center',
};

export const AlignRight = Template.bind({});
AlignRight.args = {
    align: 'right',
};

export const AlignInherit = Template.bind({});
AlignInherit.args = {
    align: 'inherit',
};

export const FamilyGT = Template.bind({});
FamilyGT.args = {
    family: 'gt',
};

export const FamilySans = Template.bind({});
FamilySans.args = {
    family: 'sans',
};

export const SizeXS = Template.bind({});
SizeXS.args = {
    size: 'xs',
};

export const SizeSM = Template.bind({});
SizeSM.args = {
    size: 'sm',
};

export const SizeMD = Template.bind({});
SizeMD.args = {
    size: 'md',
};

export const SizeLG = Template.bind({});
SizeLG.args = {
    size: 'lg',
};

export const SizeXL = Template.bind({});
SizeXL.args = {
    size: 'xl',
};

export const Bold = Template.bind({});
Bold.args = {
    bold: true,
};

export const WithTitle = Template.bind({});
WithTitle.args = {
    title: 'Title',
    size: 'xl',
};
